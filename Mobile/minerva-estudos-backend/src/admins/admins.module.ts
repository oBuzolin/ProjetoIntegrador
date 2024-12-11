import { Module } from '@nestjs/common';
import { SequelizeModule } from '@nestjs/sequelize';
import { AdminsService } from './admins.service';
import { Admin } from '../models/admin.model';

@Module({
  imports: [SequelizeModule.forFeature([Admin])],
  providers: [AdminsService],
  exports: [AdminsService, SequelizeModule],
})
export class AdminsModule {}
