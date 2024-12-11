import {
  Column,
  Model,
  Table,
  PrimaryKey,
  HasMany,
} from 'sequelize-typescript';
import { ProfessorTurma } from './professor-turma.model';
import { MatriculaTurma } from './matricula-turma.model';
import { MuralMensagem } from './mural-turma.model';

@Table({
  tableName: 'Minerva_Turma',
  timestamps: false,
})
export class Turma extends Model<Turma> {
  @PrimaryKey
  @Column
  id_turma: number;

  @Column
  nomeTurma: string;

  @HasMany(() => ProfessorTurma)
  professorTurmas: ProfessorTurma[];

  @HasMany(() => MatriculaTurma)
  matriculaTurmas: MatriculaTurma[];

  @HasMany(() => MuralMensagem)
  muralMensagens: MuralMensagem[];
}
