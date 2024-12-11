import { Module } from '@nestjs/common';
import { SequelizeModule } from '@nestjs/sequelize';
import { TurmasController } from './turmas.controller';
import { TurmasService } from './turmas.service';
import { Turma } from '../models/turma.model';
import { ProfessorTurma } from '../models/professor-turma.model';
import { AuthModule } from 'src/auth/auth.module';
import { MuralMensagem } from 'src/models/mural-turma.model';

@Module({
  imports: [
    SequelizeModule.forFeature([Turma, ProfessorTurma, MuralMensagem]),
    AuthModule,
  ],
  controllers: [TurmasController],
  providers: [TurmasService],
})
export class TurmasModule {}
