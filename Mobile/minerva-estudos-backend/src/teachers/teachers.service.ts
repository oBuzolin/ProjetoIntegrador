import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { Professor } from '../models/teacher.model';

@Injectable()
export class TeachersService {
  constructor(
    @InjectModel(Professor) private professorModel: typeof Professor,
  ) {}

  findOne(matricula: number): Promise<Professor> {
    return this.professorModel.findOne({ where: { matricula } });
  }
  findAll(): Promise<Professor[]> {
    return this.professorModel.findAll();
  }
}
