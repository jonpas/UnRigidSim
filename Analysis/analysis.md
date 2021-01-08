---
# generate pdf: `pandoc -d .pandoc.yml analysis.md`
plot-configuration: .plot.yml
title: |
    Rigid Body Simulation Scalability Analysis \
    Unreal Engine 4
---

```{.matplotlib file=plot.py caption="Amount of objects vs FPS (mode, min, max)"}
```

\vspace{1cm}

Figure 1 shows that spheres are easier on physics simulation than cubes. At 5000 objects we assume we are reaching other bottlenecks, such as rendering that many objects.

_All measurements were performed in the same scene, at the same camera location and rotation. Unreal Engine's FPS display was used._
