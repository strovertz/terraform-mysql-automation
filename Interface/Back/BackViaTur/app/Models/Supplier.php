<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;
use Carbon\Carbon;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;


/**
 * @property Carbon $deleted_at
 * @property Carbon $created_at
 * @property string $nome
 * @property float $valor
 * @property string $tipo_servico
 * @property string $endereco
 * @property string $descricao
 * @property mixed $data
 * @property string $tipo_pagamento
 */
class Supplier extends Model
{
    use HasApiTokens, HasFactory, Notifiable, SoftDeletes;

    public $primaryKey = 'id';

    public $table = 'servicos';
    public $fillable = [
        'nome',
        'data',
        'valor',
        'descricao',
        'endereco',
        'tipo_servico',
        'tipo_pagamento'
    ];

    protected $hidden = [
        'created_at',
        'deleted_at',
    ];

    public $casts = [
        'created_at' => 'datetime:d-m-Y',
        'deleted_at' => 'datetime:d-m-Y',
        'updated_at' => 'datetime:d-m-Y',
    ];

    public function mapFrontendToDatabase($data)
    {
        $columnMapping = [
            'nameSupplier' => 'nome',
            'dataService' => 'data',
            'priceService' => 'valor',
            'descriptionService' => 'descricao',
            'addressService' => 'endereco',
            'selectedOptionService' => 'tipo_servico',
            'selectedPayService' => 'tipo_pagamento',
        ];

        $columnsToUpdate = [];
        foreach ($columnMapping as $frontendField => $dbColumn) {
            if (isset($data[$frontendField])) {
                $columnsToUpdate[$dbColumn] = $data[$frontendField];
            }
        }

        return $columnsToUpdate;
    }

    public function updateSupplier($data, $id)
    {
        $columnsToUpdate = $this->mapFrontendToDatabase($data);

        $sup = self::query()
            ->where('id', '=', $id)
            ->update($columnsToUpdate);

        return $sup;
    }
}
