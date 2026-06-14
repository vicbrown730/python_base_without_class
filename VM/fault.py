class VMFault(Exception):
    pass

class LoadFault(VMFault):
    pass

class StoreFault(VMFault):
    pass

class StackFault(VMFault):
    pass

class JumpFault(VMFault):
    pass

class CallFault(VMFault):
    pass