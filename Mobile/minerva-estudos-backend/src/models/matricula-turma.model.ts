import {
  Column,
  Model,
  Table,
  PrimaryKey,
  ForeignKey,
} from 'sequelize-typescript';
import { Student } from './student.model';
import { Turma } from './turma.model';

@Table({
  tableName: 'Minerva_MatriculaTurma',
  timestamps: false,
})
export class MatriculaTurma extends Model<MatriculaTurma> {
  @PrimaryKey
  @Column
  id: number;

  @ForeignKey(() => Student)
  @Column
  ra_id: number;

  @ForeignKey(() => Turma)
  @Column
  id_turma_id: number;

  @Column
  dataMatricula: Date;
}
