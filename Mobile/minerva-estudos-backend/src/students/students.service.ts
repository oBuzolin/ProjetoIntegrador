import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { Student } from '../models/student.model';

@Injectable()
export class StudentsService {
  constructor(@InjectModel(Student) private studentModel: typeof Student) {}

  findOne(ra: number): Promise<Student> {
    return this.studentModel.findOne({ where: { ra } });
  }
  findAll(): Promise<Student[]> {
    return this.studentModel.findAll();
  }
}
