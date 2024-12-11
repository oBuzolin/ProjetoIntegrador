import { Module } from '@nestjs/common';
import { SequelizeModule } from '@nestjs/sequelize';
import { UsersService } from './user.service';
import { User } from '../models/user.model';
import { StudentsModule } from '../students/students.module';
import { TeachersModule } from 'src/teachers/teachers.module';
import { AdminsModule } from 'src/admins/admins.module';

@Module({
  imports: [
    SequelizeModule.forFeature([User]),
    StudentsModule,
    TeachersModule,
    AdminsModule,
  ],
  providers: [UsersService],
  exports: [UsersService],
})
export class UsersModule {}
