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

    def __repr__(self) -> str:
        return f'{self.apr_rel_prod} | '\
               f'{self.descricao_de_produto[:20]} | '\
               f'{self.fornec} | '\
               f'{self.cod_sap} | '\
               f'{self.sai} | '\
               f'{self.ops} | '\
               f'{self.formato} | '\
               f'{self.prv_ini} | '\
               f'{self.setup} | '\
               f'{self.acerto} | '\
               f'{self.oper} | '\
               f'{self.qtd_prev_m} | '\
               f'{self.qtf_prev_mil} | '\
               f'{self.bula} | '\
               f'{self.faca} | '\
               f'{self.mont} | '\
               f'{self.cilin} | '\
               f'{self.hot_s} | '\
               f'{self.roto} | '\
               f'{self.sit} | '\
               f'{self.entrega} | '\
               f'{self.col} | '\
               f'{self.alm} | '\
               f'{self.des} | '\
               f'{self.pre} | '\
               f'{self.cart} | '\
               f'{self.cli}'
