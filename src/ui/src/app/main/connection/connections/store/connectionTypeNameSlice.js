import { createSlice, createAsyncThunk, createEntityAdapter } from '@reduxjs/toolkit';
import axios from './axios';

export const getConnectionTypeName = createAsyncThunk('connectionsApp/connectionTypeName/getConnectionTypeName', async params => {
	// GetConnection
	const response = await axios.get('/api/Lookup/ConnectionType', {
	});
	const data = await response.data;
	return data.result.data;
});

export const connectionTypeNameAdapter = createEntityAdapter({});

export const { selectAll: selectConnectionTypeName, selectById: selectConnectionTypeNameById } = connectionTypeNameAdapter.getSelectors(
	state => state.connectionsApp.connectionTypeName
);

const connectionTypeName = createSlice({
	name: 'connectionsApp/connectionTypeName',
	initialState: connectionTypeNameAdapter.getInitialState({}),
	reducers: {},
	extraReducers: {
		[getConnectionTypeName.fulfilled]: (state, action) => {
			connectionTypeNameAdapter.setAll(state, action.payload);
		}
	}
});
export default connectionTypeName.reducer;
