import {
  Column,
  Model,
  Table,
  PrimaryKey,
  HasMany,
} from 'sequelize-typescript';
import { ProfessorTurma } from './professor-turma.model';

@Table({
  tableName: 'Minerva_Professor',
  timestamps: false,
})
export class Professor extends Model<Professor> {
  @PrimaryKey
  @Column
  matricula: number;

  @Column
  nome: string;

  @Column
  usuario: string;

  @Column
  senha: string;

  @Column
  disciplina: string;

  @Column
  cargaHoraria: number;

  @Column
  DiaSemana: string;

  @HasMany(() => ProfessorTurma)
  turmas: ProfessorTurma[];
}
