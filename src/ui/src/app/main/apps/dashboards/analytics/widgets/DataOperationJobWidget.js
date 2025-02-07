import React from 'react';
import {withStyles, Card, Icon, Typography} from '@material-ui/core';
import {Line} from 'react-chartjs-2';

const DataOperationJobWidget = ({data, theme}) => {

    const dataWithColors = data.datasets.map(obj => ({
        ...obj,
        borderColor    : theme.palette.primary.main,
        backgroundColor: theme.palette.primary.main
    }));

    return (
        <Card className="w-full rounded-8 shadow-none border-1">

            <div className="p-16 pb-0 flex flex-row flex-wrap items-end">

                <div className="pr-16">
                    <Typography className="h3" color="textSecondary">Jobs</Typography>
                    <Typography className="text-56 font-300 leading-none mt-8">
                        {data.data.value}
                    </Typography>
                </div>

                <div className="py-4 text-16 flex flex-row items-center">
                    <div className="flex flex-row items-center">
						{data.data.yesterdayDifference > 0 && <Icon className="text-green">trending_up</Icon>}
						{data.data.yesterdayDifference < 0 && <Icon className="text-red">trending_down</Icon>}
                    </div>
                </div>

            </div>

            <div className="h-96 w-100-p">
                <Line
                    data={{
                        labels  : data.labels,
                        datasets: dataWithColors
                    }}
                    options={data.options}
                />
            </div>
        </Card>
    );
};

export default withStyles(null, {withTheme: true})(DataOperationJobWidget);
