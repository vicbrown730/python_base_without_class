from fault import LoadFault

class PBInterpreter:
    
    def __init__(self, const: list[int|float|str|bool|list] = [], instruction: list[tuple[str, int]] = []):
        self.stack = []
        self.global_var = {}
        self.const = const
        self.instruction = instruction

    def run(self):
        ins_list = {"load_const": self._load_const}
        pc = 0
        pc_max = len(self.instruction)
        while pc < pc_max:
            opname, arg = self.instruction[pc]
            result = ins_list[opname](arg)
            if result == 0:
                pc += 1
                
    def _load_const(self, arg):
        try:
            self.stack.append(self.const[arg])
        except Exception:
            raise LoadFault("所加载的字面量不存在") from None
        return 0
               
        