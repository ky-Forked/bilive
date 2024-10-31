#!/bin/bash

# import the $root_path
while read key value; do
    export $key="$value"
done < ./path.txt

echo $root_path

if [ $# -gt 0 ]; then
    target_folder="$1"
else
    target_folder="$root_path/Videos"
fi

queue=("$target_folder")

while [ ${#queue[@]} -gt 0 ]; do
    current_folder=${queue[0]}
    unset queue[0]
    queue=( "${queue[@]}" )

    for file in "$current_folder"/*; do
        # echo "$file"
        if [ -d "$file" ]; then
            queue=( "${queue[@]}" "$file" )
        elif [[ $file == *.mp4 ]]; then
            absolute_mp4_path=$(readlink -f "$file")
            # echo "begin mp4 loop"
	        echo "$absolute_mp4_path"
            # echo "loop end"
            xml_file="${file%.mp4}.xml"
            if [ -f "$xml_file" ]; then
                $root_path/formatName.sh "$absolute_mp4_path"
            elif [[ $file =~ ^$root_path/Videos/[0-9]+/[0-9]+_[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}\.mp4$ ]]; then
                $root_path/uploadVideo.sh "$absolute_mp4_path"
            fi
        fi
    done
done