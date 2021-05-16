Coding diary for the interested + some Windows10 facts:
- I wanted to use `pygame`, but it natively doesn't allow multiple windows plus doesn't allow UTF-8 characters in captions
- I tried `cocos` too but it is overcomplicated for the task TBH
- `pyglet` could run multiple windows and render UTF-8 in title bar, but it (or underlying `opengl`) has a bug (or rather a feature?) that removes the new windows above 12 of them (I needed 36). 
  So I tried running the windows in different processes with `multiprocessing` module and `multiprocessing`'s build IPC, and it has finally worked. Though shit likes to consume the CPU.
- default Windows 10 (Segoe UI) font isn't monospaced but I could emulate it using different width UTF-8 space characters
- about 320 characters seems to be rendering limit for Windows titlebars (because of this bug, the whole thing took me 3x more time than it should have)
