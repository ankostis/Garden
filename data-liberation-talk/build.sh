mydir="${0%/*}"

# dump cmds executed
set -x

# build slides
hovercraft "${mydir}/data-liberation-talk.rst" "${mydir}/slides/"

# build htmpage
pandoc "${mydir}/data-liberation-talk.rst" -o "${mydir}/data-liberation-talk.html"
