from VM.PBInterpreter import PBInterpreter

Interpreter = PBInterpreter(
[
    #代码块0
    (
        ["hello", "world"],
        [
            ("load_const", 0), 
            ("load_const", 1)
        ]
    )
])

Interpreter.run()
print(Interpreter.stack)