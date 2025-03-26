# projeto2CamadaFisica

Este projeto implementa uma comunicação entre um transmissor e um servidor utilizando a camada física. Ele utiliza a conversão de números de ponto flutuante para o formato IEEE 754 para transmissão e reconversão no lado do servidor.

## Como funciona

1. **Transmissor (`transmit.py`)**:
   - Converte uma lista de números de ponto flutuante para o formato IEEE 754.
   - Envia os dados para o servidor através de uma interface serial.
   - Recebe a soma dos números calculada pelo servidor e verifica sua precisão.

2. **Servidor (`server.py`)**:
   - Recebe os dados enviados pelo transmissor.
   - Converte os bytes recebidos de volta para números de ponto flutuante.
   - Calcula a soma dos números e envia o resultado de volta ao transmissor.

3. **Conversão de dados**:
   - `floatToIEEE.py`: Converte números de ponto flutuante para o formato IEEE 754.
   - `IEEEToFloat.py`: Converte bytes no formato IEEE 754 de volta para números de ponto flutuante.

4. **Camada de enlace**:
   - `enlace.py`, `enlaceRx.py`, `enlaceTx.py`: Implementam a comunicação serial entre o transmissor e o servidor.

5. **Interface física**:
   - `interfaceFisica.py`: Gerencia a comunicação serial com a porta física.

## Requisitos

- Python 3.x
- Biblioteca `pyserial` para comunicação serial.

## Execução

1. Conecte os dispositivos de transmissão e recepção às portas seriais apropriadas.
2. Configure os nomes das portas seriais em `transmit.py` e `server.py` (`serialName`).
3. Execute primeiro o servidor:
   ```bash
   python3 server.py
   ```
4. Em seguida, execute o transmissor:
   ```bash
   python3 transmit.py
   ```

## Estrutura do Projeto

- `transmit.py`: Código do transmissor.
- `server.py`: Código do servidor.
- `floatToIEEE.py`: Conversão de float para IEEE 754.
- `IEEEToFloat.py`: Conversão de IEEE 754 para float.
- `enlace.py`, `enlaceRx.py`, `enlaceTx.py`: Implementação da camada de enlace.
- `interfaceFisica.py`: Interface com a camada física.