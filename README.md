# yak-publish

This builds and publishes any Rhino and/or Grasshopper plugins (defined by a yak specification yml) to the McNeel Package server OR test server.



# Usage

see [main.yml](https://github.com/crashcloud/yak-publish/blob/main/.github/workflows/main.yml)

**Test build and publish to test server**

``` yaml
steps:
- uses: crashcloud/yak-publish@v1
  with:
  	package-name: 'My Yak Package'
  	token: ${{ secrets.YAK_TOKEN }}
  	build-path: 'src/project/bin/**/x64/'
  	platform: win
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
    uses: crashcloud/yak-publish@v1
    with:
      package-name: 'My Yak Package'
      token: ${{ secrets.YAK_TOKEN }}
      build-path: 'src/project/bin/**/x64/''
      test-run: false
      platform: ${{ matrix.os }}      
```

**Arguments**

| Argument Name  | Expected Value             | Comments                                                     |
| -------------- | -------------------------- | ------------------------------------------------------------ |
| `package-name` | The name of the package    | Enclose in quotes if spaces exist                            |
| `token`        | `${{ secrets.YAK_TOKEN }}` | Use yak.exe --ci locally to get this token. Add to GitHub secrets. |
| `build-path`   |                            | globs accepted                                               |
| `test-run`     | true or false              | test-run uploads to the McNeel Test Server                   |
| `platform`     | windows/win or mac/mac-os  | Linux not supported                                          |



**Recommendations**

Building yak packages on the platform you intend to distribute them for leads to less potential problems.



# License

This action is all covered by the [MIT License](https://github.com/crashcloud/yak-publish/blob/main/LICENSE)
