#!/bin/bash

for i in `ls | grep '^[a-z]'`; do
  echo "========== $i =========="
  jsonschema -i "$i" ModelInformation.schema.json
done
