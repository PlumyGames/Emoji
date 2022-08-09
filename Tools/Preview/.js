#!/usr/bin/env -S deno run -A --unstable

import { output } from './Paths.js'
import discover from './Discover.js'
import combine from './Combine.js'

const { writeFile } = Deno;
const { clear , log } = console;


clear();

log('\n',`Building preview from emoji..`,'\n');


const 
    paths = await discover() ,
    combined = await combine(paths) ,
    bytes = await combined.encode() ;

await writeFile(output,bytes);


log('\n',`Finished.`,'\n');
