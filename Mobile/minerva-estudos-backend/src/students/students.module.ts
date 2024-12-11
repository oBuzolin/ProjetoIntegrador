import { Module } from '@nestjs/common';
import { SequelizeModule } from '@nestjs/sequelize';
import { StudentsService } from './students.service';
import { Student } from '../models/student.model';

@Module({
  imports: [SequelizeModule.forFeature([Student])],
  providers: [StudentsService],
  exports: [StudentsService, SequelizeModule],
})
export class StudentsModule {}
