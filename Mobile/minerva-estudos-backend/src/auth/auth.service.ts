import { Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { UsersService } from '../user/user.service';

@Injectable()
export class AuthService {
  constructor(
    private usersService: UsersService,
    private jwtService: JwtService,
  ) {}

  async validateUser(userId: string, password: string): Promise<any> {
    const userIdd = parseInt(userId);
    const userLogin = await this.usersService.findOneByUserId(userIdd);
    if (!userLogin || userLogin.status !== 'ativo') {
      throw new UnauthorizedException('User not found or inactive');
    }

    let user = null;

    if (userLogin.adm_matricula_id === userIdd) {
      user = await this.usersService.findAdminByMatricula(userIdd);
    } else if (userLogin.professor_matricula === userIdd) {
      user = await this.usersService.findProfessorByMatricula(userIdd);
    } else if (userLogin.aluno_ra === userIdd) {
      user = await this.usersService.findStudentByRA(userIdd);
    }

    if (user && this.usersService.validatePassword(user.senha, password)) {
      return user;
    }

    throw new UnauthorizedException('Invalid credentials');
  }

  async login(user: any) {
    const payload = {
      username: user.usuario,
      sub: user.matricula || user.aluno_ra || user.adm_matricula_id,
    };
    return {
      token: this.jwtService.sign(payload),
    };
  }
}
