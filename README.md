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

flow control
```mermaid
stateDiagram-v2
    [*] --> nvlc
    state nvlc {
				 data: ffprobe (get video info)
				 ffmpeg: ffmpeg (extract frames)
				 time: increment video time
       	[*] --> data
				[*] --> ffmpeg
        ffmpeg --> time : pass parameters
        time --> ffmpeg : cache
        --
				init: init /cache
				join: dealloc & join
				state B {
      	direction LR
				del: rm IMG*
				next: next IMG*++
      	jp2a --> del : print IMG* to stdout
				del --> next
				next --> jp2a
    		}
        [*] --> init
				init --> bar.sh : wait for other process to init
				bar.sh --> B
				B --> join
				join --> [*]
    }
```

## Images
[comment]: <> (hahaha)
![image]()
![image]()




