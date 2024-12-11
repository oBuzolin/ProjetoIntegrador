import {
  Column,
  Model,
  Table,
  ForeignKey,
  PrimaryKey,
  DataType,
  Default,
} from 'sequelize-typescript';
import { Professor } from './teacher.model';
import { Student } from './student.model';
import { Turma } from './turma.model';

@Table({
  tableName: 'Minerva_MuralMensagem',
  timestamps: false,
})
export class MuralMensagem extends Model<MuralMensagem> {
  @PrimaryKey
  @Column
  id: number;

  @ForeignKey(() => Student)
  @Column
  aluno_id: number;

  @ForeignKey(() => Professor)
  @Column
  professor_id: number;

  @ForeignKey(() => Turma)
  @Column
  turma_id: number;

  @Column(DataType.TEXT)
  mensagem: string;

  @Default(DataType.NOW)
  @Column(DataType.DATE)
  data_publicacao: Date;
}
