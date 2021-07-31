import React, { useEffect } from 'react';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import { getDataOperationName, selectDataOperationName } from './store/dataOperationNameSlice';
import { getDataOperations } from './store/dataOperationsSlice';
import Button from '@material-ui/core/Button';
import Autocomplete, { createFilterOptions } from '@material-ui/lab/Autocomplete';
import { filterFormStyles } from '../../common/styles/FilterFormStyles';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';




function DataOperationsFilterForm() {
	const dispatch = useDispatch();
	const classes = filterFormStyles();
	const filterOptions = createFilterOptions({
		matchFrom: 'start',
		stringify: option => {
			return option.name
		},
	});
	const routeParams = useParams();

	useEffect(() => {
		dispatch(getDataOperationName(routeParams));
	}, [dispatch, routeParams]);

	//states
	const [dataOperation, setDataOperation] = React.useState(null);
	const selectDataOperationNames = useSelector(selectDataOperationName);


	const [onlyUndeleted, setOnlyUndeleted] = React.useState(true);
	const handleOnlyUndeletedChange = (event) => {
		setOnlyUndeleted(event.target.checked);
	};


	const clear = event => {
		setDataOperation(null);
		setOnlyUndeleted(true);

		routeParams.DataOperationId = null;
		routeParams.OrderBy = "DataOperation.Id";
		routeParams.PageNumber = 1;
		routeParams.Order = null;
		routeParams.OnlyUndeleted = true;
		dispatch(getDataOperations(routeParams));
	};

	const filter = event => {

		let dataOperationName = null;
		if (dataOperation != null) {
			dataOperationName = dataOperation.name;
		}
		routeParams.DataOperationName = dataOperationName;

		routeParams.PageNumber = 1;
		routeParams.OnlyUndeleted = onlyUndeleted;
		dispatch(getDataOperations(routeParams));
	};




	return (

		<div className={classes.root}
			style={{ padding: '15px 40px 15px 40px' }}
		>
			<div className="flex flex-col flex-shrink-0 sm:flex-row items-center justify-between py-10"></div>
			<Grid container spacing={3}>
				<Grid item xs>
					<Autocomplete
						id="country-select-demo"
						style={{ width: '100%' }}
						value={dataOperation}
						onChange={(event, newValue) => {
							setDataOperation(newValue);
						}}
						options={selectDataOperationNames}
						classes={{
							option: classes.option,
						}}
						filterOptions={filterOptions}
						getOptionLabel={(option) => option.name}
						renderOption={(option) => (
							<React.Fragment>
								<span>{option.name}</span>
							</React.Fragment>
						)}
						renderInput={(params) => (
							<TextField
								{...params}
								label="DataOperation "
								variant="outlined"
								inputProps={{
									...params.inputProps,
									autoComplete: 'new-password', // disable autocomplete and autofill
								}}
							/>
						)}
						autoHighlight
						clearOnEscape
						openOnFocus
					/>
				</Grid>
				<Grid item xs>
					<FormGroup row>
						<FormControlLabel style={{ margin: "5px" }}
							control={<Checkbox checked={onlyUndeleted} onChange={handleOnlyUndeletedChange} name="onlyUndeleted" />}
							label="Only Undeleted"
						/>
					</FormGroup>
				</Grid>
				<Grid item xs>
				</Grid>
				<Grid item xs>
				</Grid>
			</Grid>

			<Grid container spacing={3}>
				<Grid item xs>
				</Grid>
				<Grid item xs={1}>
					<Button
						variant="contained"
						color="secondary"
						size="large"
						className={classes.button}
						// startIcon={<SearchIcon />}
						onClick={clear}
					>
						Clear
					</Button>
				</Grid>
				<Grid item xs={1}>
					<Button
						variant="contained"
						color="secondary"
						size="large"
						className={classes.button}
						// startIcon={<SearchIcon />}
						onClick={filter}
					>
						Search
					</Button>
				</Grid>
			</Grid>
		</div>
	);
}
export default DataOperationsFilterForm;
