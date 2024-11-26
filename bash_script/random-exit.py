#!/usr/bin/env python

import sys
import random



val=random.randint(0,1)
print(f"Retrying: {str(val)}")
sys.exit(val)