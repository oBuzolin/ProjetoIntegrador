import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/sequelize';
import { Turma } from '../models/turma.model';
import { ProfessorTurma } from '../models/professor-turma.model';
import { MuralMensagem } from '../models/mural-turma.model';

@Injectable()
export class TurmasService {
  constructor(
    @InjectModel(Turma) private turmaModel: typeof Turma,
    @InjectModel(ProfessorTurma)
    private professorTurmaModel: typeof ProfessorTurma,
    @InjectModel(MuralMensagem)
    private muralTurmaModel: typeof MuralMensagem,
  ) {}

  async findTurmaByProfessorId(professorId: number): Promise<Turma[]> {
    console.log('Professor ID:', professorId); // Log do ID do professor

    const professorTurmas = await this.professorTurmaModel.findAll({
      attributes: ['matricula', 'id_turma'],
      where: { matricula: professorId },
    });
    console.log('ProfessorTurmas encontrados:', professorTurmas); // Log dos resultados de ProfessorTurma

    const turmaIds = professorTurmas.map((pt) => pt.id_turma);
    console.log('IDs das turmas associadas:', turmaIds); // Log dos IDs das turmas

    const turmas = await this.turmaModel.findAll({
      where: { id_turma: turmaIds },
      include: [{ model: MuralMensagem }],
    });
    console.log('Turmas encontradas:', JSON.stringify(turmas, null, 2)); // Log das turmas encontradas

    return turmas;
  }
}
