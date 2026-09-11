# Especificação: Sistema de Cálculo de Frete

## Requisitos Não Funcionais
RNF-01: THE SYSTEM SHALL calculate the shipping cost in <100ms

## Requisitos Funcionais
RF-01: WHEN total cost >= total cost limit, THE SYSTEM SHALL set shipping cost to RS0,00

RF-02: IF shipping cost >RS15,00 THEN reduce shipping cost by 20%

RF-03: IF shipping cost >RS100,00, THEN reduce shipping cost by 100%

## Requisitos de Negócio
RB-01: WHILE região = 'Norte', total cost limit will be RS300,00. Other values for região: RS200,00.

RB-02: IF total cost <= RS0,00, THEN show error "Carrinho inválido."



