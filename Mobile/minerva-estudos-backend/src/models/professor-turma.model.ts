import { Column, Model, Table, ForeignKey } from 'sequelize-typescript';
import { Professor } from './teacher.model';
import { Turma } from './turma.model';

@Table({
  tableName: 'Minerva_ProfessorTurma',
  timestamps: false,
})
export class ProfessorTurma extends Model<ProfessorTurma> {
  @ForeignKey(() => Professor)
  @Column
  matricula: number;

  @ForeignKey(() => Turma)
  @Column
  id_turma: number;
}
