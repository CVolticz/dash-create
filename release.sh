release_type=$1

TAG=$(git describe --tags --abbrev=0)
MINOR=$(echo $TAG | sed -E 's|^.*\.([0-9]+)$|\1|')
MAJOR=$(echo $TAG | sed -E 's|^v(.*)\.[0-9]+$|\1|')


if [[ "$release_type" =~ ^(major|minor)$ ]]; then
    echo "Releasing $release_type update"
    if [ "$release_type" == "minor" ]; then
        NEWVER="$((MAJOR)).$((MINOR+1))"
    elif [ "$release_type" == "major" ]; then
        NEWVER="$((MAJOR+1)).0"

    fi
fi
echo "new version v$NEWVER"

git tag v$NEWVER
git push origin v$NEWVER

