import { Module } from '@nestjs/common';
import { SequelizeModule } from '@nestjs/sequelize';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './user/user.module';
import { StudentsModule } from './students/students.module';
import { TeachersModule } from './teachers/teachers.module';
import { AdminsModule } from './admins/admins.module';
import { TurmasModule } from './turmas/turmas.module';
import { User } from './models/user.model';
import { Student } from './models/student.model';
import { Professor } from './models/teacher.model';
import { Admin } from './models/admin.model';
import { Turma } from './models/turma.model';
import { ProfessorTurma } from './models/professor-turma.model';
import { MatriculaTurma } from './models/matricula-turma.model';
import { MuralMensagem } from './models/mural-turma.model';

@Module({
  imports: [
    SequelizeModule.forRoot({
      dialect: 'mysql',
      host: '143.106.241.3',
      port: 3306,
      username: 'cl201107',
      password: 'cl*02032005',
      database: 'cl201107',
      models: [
        User,
        Student,
        Professor,
        Admin,
        Turma,
        ProfessorTurma,
        MatriculaTurma,
        MuralMensagem,
      ],
      autoLoadModels: true,
      synchronize: true,
    }),
    AuthModule,
    UsersModule,
    StudentsModule,
    TeachersModule,
    AdminsModule,
    TurmasModule,
  ],
})
export class AppModule {}
