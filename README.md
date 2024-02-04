# yak-publish

This builds and publishes any Rhino and/or Grasshopper plugins (defined by a yak specification yml) to the McNeel Package server OR test server, OR nowhere!


# Usage
You will need to make sure you define `YAK_TOKEN` in your environment variables following this guide : https://discourse.mcneel.com/t/github-action-to-yak/120815/2 (if you wish to publish!).

see [action.yml](https://github.com/crashcloud/yak-publish/blob/main/.github/workflows/action.yml)

# Build Configuration Specifics

## Rhino 7
Rhino 7 requires a simple net48 directory with icon and manifest in it
```
└── net48
    ├── *.dll
    ├── *.rhp
    ├── icon.png
    └── manifest.yml
```

## Rhino 8 multi-targeted
Multi-target Rhino 8 requires net48 and net7.0+ directories.

This is the ideal configuration
```
├── icon.png
├── manifest.yml
├── net48
│   ├── *.dll
│   ├── *.rhp
└── net7.0
    ├── *.dll
    └── *.rhp
```

This is also a supported build configuration, yak-publish will convert it into the above. **Unique Manifests (per configuration) are not supported or a good idea**.
```
├── net48
│   ├── *.dll
│   ├── *.rhp
│   ├── icon.png
│   └── manifest.yml
└── net7.0
    ├── *.dll
    ├── *.rhp
    ├── icon.png
    └── manifest.yml
```

**Test build and publish to test server**

``` yaml
steps:
- uses: crashcloud/yak-publish@main
  with:
  	package-name: 'My Yak Package'
  	token: ${{ secrets.YAK_TOKEN }}
  	build-path: 'src/**/bin/**/**/'
  	publish: 'test'
```

**Cross-platform build and publish to production server**

``` yaml
strategy:
  matrix:
    os: [ 'windows', 'mac-os' ]
runs-on: ${{ matrix.os }}
name: Yak Build & Publish
steps:
  - id: yak
    uses: crashcloud/yak-publish@main
    with:
      package-name: 'My Yak Package'
      token: ${{ secrets.YAK_TOKEN }}
      build-path: 'src/project/bin/**/x64/'
      publish: 'production'
```

**Arguments**

| Argument Name  | Expected Value             | Comments                                                                                                                   |
| -------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------|
| `package-name` | The name of the package    | Enclose in quotes if spaces exist                                                                                          |
| `token`        | `${{ secrets.YAK_TOKEN }}` | Use yak.exe --ci locally to get this token. Add to GitHub secrets.                                                         |
| `build-path`   |                            | globs accepted                                                                                                             |
| `publish`     | '', 'test', 'production'              | '' publishes nothing, 'test' published to the the McNeel Test Server. 'production' published to the real yak package server|



**Recommendations**

Building yak packages on the platform you intend to distribute them for leads to less potential problems.



# License

This action is all covered by the [MIT License](https://github.com/crashcloud/yak-publish/blob/main/LICENSE)
