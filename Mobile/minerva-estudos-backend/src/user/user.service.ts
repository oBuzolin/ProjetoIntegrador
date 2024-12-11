import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { Op } from 'sequelize';
import { User } from '../models/user.model';
import { Student } from '../models/student.model';
import { Professor } from '../models/teacher.model';
import { Admin } from '../models/admin.model';
import * as crypto from 'crypto';

@Injectable()
export class UsersService {
  constructor(
    @InjectModel(User) private userModel: typeof User,
    @InjectModel(Student) private studentModel: typeof Student,
    @InjectModel(Professor) private professorModel: typeof Professor,
    @InjectModel(Admin) private adminModel: typeof Admin,
  ) {}

  async findOneByUserId(userId: number): Promise<User> {
    return this.userModel.findOne({
      attributes: [
        'id',
        'adm_matricula_id',
        'professor_matricula',
        'aluno_ra',
        'status',
      ],
      where: {
        [Op.or]: [
          { adm_matricula_id: userId },
          { professor_matricula: userId },
          { aluno_ra: userId },
        ],
      },
    });
  }

  async findStudentByRA(ra: number): Promise<Student> {
    return this.studentModel.findOne({
      where: { ra },
      attributes: ['ra', 'senha'],
    });
  }

  async findProfessorByMatricula(matricula: number): Promise<Professor> {
    return this.professorModel.findOne({
      where: { matricula },
      attributes: ['matricula', 'senha'],
    });
  }

  async findAdminByMatricula(matricula: number): Promise<Admin> {
    return this.adminModel.findOne({
      where: { matricula },
      attributes: ['matricula', 'senha'],
    });
  }

  validatePassword(storedHash: string, providedPassword: string): boolean {
    const hash = crypto
      .createHash('sha256')
      .update(providedPassword)
      .digest('hex');
    return storedHash === hash;
  }
}
