import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { Admin } from '../models/admin.model';

@Injectable()
export class AdminsService {
  constructor(@InjectModel(Admin) private adminModel: typeof Admin) {}

  findOne(matricula: number): Promise<Admin> {
    return this.adminModel.findOne({ where: { matricula } });
  }
  findAll(): Promise<Admin[]> {
    return this.adminModel.findAll();
  }
}
