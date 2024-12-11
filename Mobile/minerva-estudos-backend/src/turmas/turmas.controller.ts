import { Controller, Get, UseGuards, Request } from '@nestjs/common';
import { AuthGuard } from '../auth/guards/auth.guard';
import { TurmasService } from './turmas.service';

@Controller('turmas')
export class TurmasController {
  constructor(private turmasService: TurmasService) {}

  @UseGuards(AuthGuard)
  @Get()
  async findTurmas(@Request() req) {
    const userId = parseInt(req.user.sub, 10);
    console.log('User ID:', userId); // Log do ID do usuário
    const turmas = await this.turmasService.findTurmaByProfessorId(userId);
    console.log(
      'Turmas retornadas pelo serviço:',
      JSON.stringify(turmas, null, 2),
    ); // Log das turmas retornadas pelo serviço
    // Transformar os dados para uma estrutura mais simples antes de enviar
    const turmasSimplificadas = turmas.map((t) => ({
      id_turma: t.id_turma,
      nomeTurma: t.nomeTurma,
      muralMensagens: t.muralMensagens.map((m) => ({
        id: m.id,
        aluno_id: m.aluno_id,
        professor_id: m.professor_id,
        mensagem: m.mensagem,
        data_publicacao: m.data_publicacao,
      })),
    }));
    console.log(
      'Turmas retornadas simplificadas:',
      JSON.stringify(turmasSimplificadas, null, 2),
    ); // Log das turmas simplificadas
    return turmasSimplificadas;
  }
}
