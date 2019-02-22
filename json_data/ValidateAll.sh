#!/bin/bash
# Written by Jetho Lee

for i in `ls | grep '^[a-z]'`; do
  echo "========== $i =========="
  jsonschema -i "$i" ModelInformation.schema.json
done
