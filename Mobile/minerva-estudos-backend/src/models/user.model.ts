import {
  Column,
  Model,
  Table,
  PrimaryKey,
  AutoIncrement,
} from 'sequelize-typescript';

@Table({
  tableName: 'Minerva_Login',
  timestamps: false,
})
export class User extends Model<User> {
  @PrimaryKey
  @Column
  id: number;

  @Column
  adm_matricula_id: number;

  @Column
  professor_matricula: number;

  @Column
  aluno_ra: number;

  @Column
  status: 'ativo' | 'cancelado' | 'bloqueado';
}
