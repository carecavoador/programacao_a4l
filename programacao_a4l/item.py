from dataclasses import dataclass, field


@dataclass
class Item:
    apr_rel_prod: str
    descricao_de_produto: str
    fornec: str
    cod_sap: int
    sai: str
    ops: int
    formato: str
    prv_ini: str
    setup: str
    acerto: str
    oper: str
    qtd_prev_m: str
    qtf_prev_mil: str
    bula: str
    faca: str
    mont: str
    cilin: str
    sit: str
    entrega: str
    col: str
    alm: str
    des: str
    pre: str
    cart: str
    cli: str
    hot_s: str = field(default=None)
    roto: str = field(default=None)

    def __str__(self) -> str:
        return f'{self.apr_rel_prod:11} | '\
               f'{self.descricao_de_produto[:20]} | '\
               f'{self.fornec} | '\
               f'{self.cod_sap} | '\
               f'{self.sai} | '\
               f'{self.ops} | '\
               f'{self.formato:6} | '\
               f'{self.prv_ini} | '\
               f'{self.setup} | '\
               f'{self.acerto} | '\
               f'{self.oper} | '\
               f'{self.qtd_prev_m:10} | '\
               f'{self.qtf_prev_mil:5} | '\
               f'{self.bula} | '\
               f'{self.faca} | '\
               f'{self.mont} | '\
               f'{self.cilin:3} | '\
               f'{self.hot_s} | '\
               f'{self.roto} | '\
               f'{self.sit} | '\
               f'{self.entrega} | '\
               f'{self.col:2} | '\
               f'{self.alm:2} | '\
               f'{self.des:2} | '\
               f'{self.pre:2} | '\
               f'{self.cart:2} | '\
               f'{self.cli:2}'
