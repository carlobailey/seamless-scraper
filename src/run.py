import pandas as pd
from page_crawler import PageCrawler
import os
import argparse


def main(args):
    coords = args.coords
    coords = zip(coords[0::2], coords[1::2])
    errors = 0
    dfs = []
    for point in coords:
        lng = point[1]
        lat = point[0]
        url = ('https://www.seamless.com/search?orderMethod=pickup&locationMode=PICKUP'
               '&facetSet=umamiV2&pageSize=20&hideHateos=true&searchMetrics=true&latitude=%s'
               '&longitude=%s&preciseLocation=true&sorts=distance&radius=1')
        pc = PageCrawler(url, headless=True, lat=lat, lng=lng, ll=5, ul=15)
        data = pc.crawl_page()
        if data is not None:
            try:
                frame = pd.DataFrame(data)
                dfs.append(frame)
            except:
                print('Error creating final dataframe')
                errors += 1
                continue
        print("process complete! there were %s errors." % errors)
    pd.concat(dfs).to_csv('%s.csv' % args.filename, index=False)

def parse_arguments():
    cli = argparse.ArgumentParser()
    cli.add_argument(
        "--coords",
        nargs="*",
        type=float,
        default=[40.674792, -73.975310],
    )

    cli.add_argument(
        "--filename",
        nargs="?",
        type=str,
        default="seamless_data",
    )

    args = cli.parse_args()
    return args

if __name__ == '__main__':
    job_args = parse_arguments()
    main(job_args)
