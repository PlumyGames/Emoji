
import { emojis } from './Paths.js'
import { walk } from 'https://deno.land/std@0.151.0/fs/mod.ts';



export default async function discover(){
    
    const options = {
        includeFiles : true ,
        includeDirs : false
    }

    const paths = [];

    for await (const entry of walk(emojis,options))
        paths.push(entry.path);
        
    return paths;
}