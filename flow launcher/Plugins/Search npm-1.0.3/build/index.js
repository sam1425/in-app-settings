var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import open from 'open';
import axios from 'axios';
import { Flow } from 'flow-launcher-helper';
import { api } from './api.js';
const { params, showResult, on, run } = new Flow('app.png');
on('query', () => __awaiter(void 0, void 0, void 0, function* () {
    if (params.length <= 1) {
        return showResult({
            title: 'Waiting for query...',
        });
    }
    try {
        const { data } = yield api.get('/search', {
            params: {
                q: params,
            },
        });
        const results = [];
        data.results.forEach(({ package: result }) => {
            results.push({
                title: `${result.name} | v${result.version}`,
                subtitle: result.description,
                method: 'open_result',
                params: [result.links.npm],
                iconPath: 'app.png',
            });
        });
        showResult(...results);
    }
    catch (err) {
        if (axios.isAxiosError(err) || err instanceof Error) {
            return showResult({
                title: 'Error',
                subtitle: err.message,
            });
        }
    }
}));
on('open_result', () => {
    const url = params;
    open(url);
});
run();
