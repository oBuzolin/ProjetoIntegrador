import { Controller, Post, Body, UnauthorizedException } from '@nestjs/common';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('login')
  async login(@Body() credentials: any) {
    const user = await this.authService.validateUser(
      credentials.userId,
      credentials.password,
    );
    if (user) {
      return this.authService.login(user);
    } else {
      throw new UnauthorizedException('Invalid credentials');
    }
  }
}
