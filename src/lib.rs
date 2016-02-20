//! EMBEDDING RUST IN PYTHON
//! Examples on how to write Rust libraries callable by a Python script.
//!
//! Author: Davide Aversa <thek3nger@gmail.com>
//! ---------------------------------------------------------------------------


/// Libc provides several C-friendly data types. This is used to write 
/// functions callable by an external languages **or** to call external
///C libraries.  
extern crate libc;

/// Use this to load in the namespace the `size_t` and `int32_t` types.
use libc::{size_t,int32_t};

/// Use this to load the standard library interface to threading.
use std::thread;

/// The first function we want to try is a simple no-input/no-outut function.
///
/// The algorithm spawns 10 threads, and each one will increas a counter
/// 5 milion times in order to simulate some work. At the end the function
/// waits for the thread completitions and retun nothing. 
#[no_mangle]
pub extern fn process() {
    let handles: Vec<_> = (0..10).map(|_| {
        thread::spawn(|| {
            let mut x = 0;
            for _ in 0..5_000_000 {
                x += 1
            }
            x
        })
    }).collect();

    for h in handles {
        println!("Thread finished with count={}",
        h.join().map_err(|_| "Could not join a thread!").unwrap());
    }
}

/// This is the next logical step, write a function who receive an integral
/// input and return nothing.
///
/// This time the algorithm spawns the number of threads passed as an argument.
/// Note that the function does not take a generic Rust i32 **but** the libc
/// defined type `int32_t`; the equivalent in the C interface for i32.
#[no_mangle]
pub extern fn process2(threads_number: int32_t) {
    let handles: Vec<_> = (0..threads_number).map(|_| {
        thread::spawn(|| {
            let mut x = 0;
            for _ in 0..5_000_000 {
                x += 1
            }
            x
        })
    }).collect();

    for h in handles {
        println!("Thread finished with count={}",
        h.join().map_err(|_| "Could not join a thread!").unwrap());
    }
}