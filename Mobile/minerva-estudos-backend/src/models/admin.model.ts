import { Column, Model, Table, PrimaryKey } from 'sequelize-typescript';

@Table({
  tableName: 'Minerva_Administrador',
  timestamps: false,
})
export class Admin extends Model<Admin> {
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
  cargo: string;
}
