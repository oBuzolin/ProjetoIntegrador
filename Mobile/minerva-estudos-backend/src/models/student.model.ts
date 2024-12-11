import { Column, Model, Table, PrimaryKey } from 'sequelize-typescript';

@Table({
  tableName: 'Minerva_Aluno',
  timestamps: false,
})
export class Student extends Model<Student> {
  @PrimaryKey
  @Column
  ra: number;

  @Column
  nome: string;

  @Column
  usuario: string;

  @Column
  senha: string;

  @Column
  curso: string;
}
