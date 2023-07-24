
def distance(p1, p2):
    # Calculates the Euclidean Distance between two points
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def centroid(points):
    # Computes the centroid of a set of points.
    # The centroid is the "average" point in the set.
    # That is, its x coordinate is the average x among the points in the set
    # and the y coordinate is the average y among the points in the set.
    xsum = 0
    ysum = 0
    for i in points:
        xsum+=i[0]
        ysum+=i[1]
    return (xsum/len(points), ysum/len(points))

def cluster(reference, points):
    # Clusters the given points using the reference points.
    # Points in the same cluster should be closest to the same reference point.
    # In other words, if points A and B are in cluster i then they should both be
    # closer to reference point i than any of the other reference points.
    s = {}
    for i in reference:
        s[i] = []
    for point in points:
        closest = reference[0]
        smallestDist = distance(reference[0], point)
        for ref in reference:
            if distance(ref, point) <= smallestDist:
                smallestDist = distance(ref, point)
                closest = ref
        s[closest].append(point)

    ans = []
    for i in s:
        ans.append(s[i])
    return ans

def k_means(k, points):
    # Performs the k-means clustering.
    reference_points = []
    vals = []
    i = 0
    while len(reference_points) < k:
        if points[i][1] not in vals:
            reference_points.append(points[i])
            vals.append(points[i][1])
        i+=1
    # our initial reference points
    # Using the reference points, cluster the points
    clusters = cluster(reference_points, points)
    # calculate the new reference points by finding the centroid of each cluster
    prev = reference_points
    reference_points = sorted([centroid(c) for c in clusters])
    # re-cluster the points using the centroids
    clusters = cluster(reference_points, points)
    while prev != reference_points:
        prev = sorted(reference_points)
    # repeat until the centroids do not change between iterations.
        clusters = cluster(reference_points, points)
        reference_points = sorted([centroid(c) for c in clusters])
    # return a list of lists of points representing the clusters.
    return clusters