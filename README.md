# Sistema de Notificações Assíncronas com FastAPI e RabbitMQ

Este projeto foi desenvolvido como parte de um teste técnico para vaga de Desenvolvedor Backend (Python). 
O objetivo principal é criar um sistema de notificações com processamento assíncrono em múltiplas etapas, utilizando FastAPI e RabbitMQ.

Descrição

A API permite o envio de notificações que são processadas de forma assíncrona por uma cadeia de consumidores RabbitMQ. 
O sistema simula falhas, tenta reprocessamentos e lida com uma fila de "dead letter" (DLQ) para mensagens irrecuperáveis. 
Todo o status de cada notificação é mantido em memória e pode ser consultado por um endpoint.
