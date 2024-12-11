import { Module } from '@nestjs/common';
import { SequelizeModule } from '@nestjs/sequelize';
import { TeachersService } from './teachers.service';
import { Professor } from '../models/teacher.model';

@Module({
  imports: [SequelizeModule.forFeature([Professor])],
  providers: [TeachersService],
  exports: [TeachersService, SequelizeModule],
})
export class TeachersModule {}
