# mappsite

mappsite has the target to provide the hierarchical structure of a given website. It works bruteforcing all possible paths and testing its relative requests. 

# Development 
Run mappsite package from / : `python -m mappsite`
Test & Debug : `nosetests tests`

- [ ] connect function checking whether the resources exist
- [ ] get std input form command line
- [ ] update tree data structure when new valid link is found
- [ ] store result in file (after ^C)
- [ ] how to write documentation in `/docs` 
- [ ] automatic, timeout and manuel mode

flow control
```mermaid
stateDiagram-v2    
    
    mappsite --> mode1
    mappsite --> mode2
    mappsite --> mode3

    mode1: automatic mode
    bruteforce1: iterate over X char string
    mode2: timeout mode
    mode3: manual mode
    
    state bruteforce1 {
      	[*] --> A{establish connection}
      	A --> B[webpage exists**]
      	B --> C[save to tree]
      	A --> D[else** - skip ]
    }
    
    state mode1 {
    
        bruteforce1 --> timeout{if timeout has expired}
        timeout -. no .-> A[explore nested links]
        A --> bruteforce1
        timeout -. yes .-> [*]
    }
    
    state mode2 {
    
    
    }
    
    state mode3 {
    
    
    
    }
```

## Images
[comment]: <> (hahaha)
![image]()
![image]()




