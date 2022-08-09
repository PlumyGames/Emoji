#!/usr/bin/env -S deno run -A --unstable


import * as Image from 'https://deno.land/x/imagescript@v1.2.14/mod.ts'

import { fromFileUrl , dirname , join } from 'https://deno.land/std@0.151.0/path/mod.ts'
import { walk } from 'https://deno.land/std@0.151.0/fs/mod.ts';



const { clear , log } = console;

const 
    folder = dirname(fromFileUrl(import.meta.url)) ,
    root = join(folder,'..','..') ,
    emojis = join(root,'emoji') ,
    output = join(root,'Resources','Preview.png');

clear();

log('\n',`Building preview from emoji..`,'\n');


const options = {
    includeFiles : true ,
    includeDirs : false
}

const paths = [];

for await (const entry of walk(emojis,options))
    paths.push(entry.path);

const 
    rows = Math.ceil(paths.length / 9) ,
    height = rows * 57 + (rows - 1) * 9 ;


log('\n',`Using ${ paths.length } emoji ➞ 600 x ${ height }px`,'\n');


let combined = new Image.Image(600,height);

let
    x = 0 ,
    y = 0 ;

for(const path of paths){
    
    const bytes = await Deno.readFile(path);
    
    const image = await Image.decode(bytes);

    const
        X = x * (57 + 9) ,
        Y = y * (57 + 9) ;

    combined = combined.composite(image,X,Y); 
    
    x++;
    
    if(x < 9)
        continue;
        
    x = 0;
    y++;
}


const bytes = await combined.encode();

await Deno.writeFile(output,bytes);

log('\n',`Finished.`,'\n');
