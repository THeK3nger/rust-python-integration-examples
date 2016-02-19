# Python-Rust Integration Example

This is an example for integrating a **Rust library in a Python script**. This will allow Python to execute binary compiled and **true multi-thread** code. Useful to execute CPU-intensive computation inside a Python script.

Distributing binary dependencies for Python script is made extremely easy by the Rust's Cargo package manager. Just execute `cargo build` before executing the Python script and Cargo will fetch all the dependencies for you. Way better than C. :D  

## Compatibility 

The Rust code is multiplatform. The Python code works on Windows. Should be easy to make this multiplatform too, and probably I will.