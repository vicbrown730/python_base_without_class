from VM.fault import LoadFault

STD_CONST_LIST = list[str|int|float|bool|list]
STD_INSTRUCTION_LIST = list[tuple[str, int]]
STD_INSTRUCTION_BLOCK = tuple[STD_CONST_LIST, STD_INSTRUCTION_LIST]

class PBInterpreter:
    
    def __init__(self, instruction: list[STD_INSTRUCTION_BLOCK] = []):
        self.stack = []
        self.global_var = {}
        self.instruction = instruction
        self.const = []

    def run(self):
        instruction_block = 0
        ins_list = {"load_const": self._load_const}
        pc = 0
        consts, insts = self.instruction[instruction_block]
        self.const = consts
        pc_max = len(insts)
        while pc < pc_max:
            opname, arg = insts[pc]
            result = ins_list[opname](arg)
            if result == 0:
                pc += 1
                
    def _load_const(self, arg):
        try:
            self.stack.append(self.const[arg])
        except Exception:
            raise LoadFault("所加载的字面量不存在") from None
        return 0
               
        